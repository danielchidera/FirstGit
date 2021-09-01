const express = require("express");
const port = 2090;

const app = express();

app.get("/", (req, res)=> {
    res.send("hi guys")
});

app.get("/json", (req, res)=> {
    res.json({message: "new api using mongoose database"})
})

app.listen(port, ()=>{
    console.log("server listening to port " + port)
})