import express from "express";
import Booking from "../models/Booking.js";

const router = express.Router();

router.post("/", async (req, res) => {
  const booking = new Booking(req.body);
  await booking.save();
  res.json({ message: "Booking Created" });
});

router.get("/", async (req, res) => {
  const bookings = await Booking.find();
  res.json(bookings);
});

router.put("/:id", async (req, res) => {
  await Booking.findByIdAndUpdate(req.params.id, req.body);
  res.json({ message: "Booking Updated" });
});

router.delete("/:id", async (req, res) => {
  await Booking.findByIdAndDelete(req.params.id);
  res.json({ message: "Booking Deleted" });
});

export default router;
