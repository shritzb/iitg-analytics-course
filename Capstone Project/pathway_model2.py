import pathway as pw

class ParkingSchema(pw.Schema):
    SystemCodeNumber: str
    Latitude: float
    Longitude: float
    Capacity: int
    Occupancy: int
    QueueLength: int
    VehicleType: str
    TrafficConditionNearby: str
    IsSpecialDay: int
    LastUpdatedDate: str
    LastUpdatedTime: str
    Timestamp: str

data = pw.io.csv.read(
    "sample_100.csv",
    schema=ParkingSchema,
    mode="static"
)
@pw.udf
def encode_traffic(t): return {"low": 0, "medium": 0.5, "high": 1}.get(t, 0)

@pw.udf
def encode_vehicle(v): return {"car": 1.0, "bike": 0.6, "truck": 1.5}.get(v, 1.0)

data = data.with_columns(
    TrafficScore = encode_traffic(data.TrafficConditionNearby),
    VehicleScore = encode_vehicle(data.VehicleType),
    OccRatio = data.Occupancy / data.Capacity
)

@pw.udf
def compute_demand(occ, queue, special, traffic, vehicle):
    return 3*occ + 0.5*queue + 1.5*special + 1.2*traffic + 1.0*vehicle

@pw.udf
def normalize(d): return (d - 2) / (15 - 2)

@pw.udf
def final_price(norm): return min(max(10 * (1 + 0.5 * norm), 5), 20)

# Step 1: Add RawDemand separately
data = data.with_columns(
    RawDemand = compute_demand(
        data.OccRatio,
        data.QueueLength,
        data.IsSpecialDay,
        data.TrafficScore,
        data.VehicleScore
    )
)
# Step 2: Now add NormDemand and DemandPrice
data = data.with_columns(
    NormDemand = normalize(data.RawDemand),
    DemandPrice = final_price(normalize(data.RawDemand))
)
pw.io.jsonlines.write(
    data.select(
        data.SystemCodeNumber,
        data.Timestamp,
        data.Occupancy,
        data.Capacity,
        data.DemandPrice
    ),
    "model2_output.jsonl"
)

pw.run()
