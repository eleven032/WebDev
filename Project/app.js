const express = require("express");
var path = require('path');
const bodyParser = require("body-parser");
const taskController = require("./controllers/TaskController");

// db instance connection
require("./config/db");

const app = express();

const port = process.env.PORT || 3301;
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// API ENDPOINTS
app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, '../project/public', 'homepage.html'))
})



app
  .route("/tasks")
  .get(taskController.listAllTasks)
  .post(taskController.createNewTask);

app
  .route("/tasks/:taskid")
  .get(taskController.readTask)
  .put(taskController.updateTask)
  .delete(taskController.deleteTask);

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});