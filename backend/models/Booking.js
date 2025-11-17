import mongoose from "mongoose";

const bookingSchema = new mongoose.Schema({
  userId: String,
  vehicleModel: String,
  serviceType: String,
  date: String,
  status: { type: String, default: "Pending" }
});

export default mongoose.model("Booking", bookingSchema);
