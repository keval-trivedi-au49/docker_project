const express = require("express");
const path = require("path");
const { BACKEND_URL } = require("./config.js");

const app = express();

function healthCheck(req, res) {
  res.set("Cache-Control", "no-store");
  res.status(200).json({
    status: "ok",
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
  });
}

app.get("/health", healthCheck);

app.get("/config.js", (req, res) => {
  res.type("application/javascript");
  res.send(`window.BACKEND_URL = ${JSON.stringify(BACKEND_URL)};`);
});

app.use(express.static(path.join(__dirname, "public")));

app.listen(3000, ()=>{
    console.log("Frontend is running on port 3000")
});
