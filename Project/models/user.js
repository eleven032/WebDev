const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const userSchema = new Schema({
  name:{
      type: String,
      required:true
  },
  year:{
      type: Number,
      required:true
  }
});

module.exports = mongoose.model("Users", userSchema);