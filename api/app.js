// Definitions
const express = require("express"),
    cors = require("cors"),
    app = express();


app.use(cors());

/// OAuth2 
const fetch = require("node-fetch")

require("dotenv").config()
const PORT = process.env.PORT || '80';


// api things 


var corsOptions = {
    origin: '*',
    optionsSuccessStatus: 200
}

const name = require("../package.json").name,
    description = require("../package.json").description,
    version = require("../package.json").version,
    author = require("../package.json").author,
    url = require("../package.json").repository.url;

// ROUTES
app.get("/", cors(corsOptions), (req, res) => {
    const mainpage = ({"API": `${name}`, "\description": `${description}`, "API Version is": `${version}`, "Github Repository": `${url}` });
    return res.send(mainpage)
});


app.get("/api/v1", cors(corsOptions), (req, res) => {
    const v1page = (`Oops! That looks like, some arguments are missing! soontm comes the Documentation`);
    return res.send(v1page) 
});



app.use(function (req, res, next) {
    res.status(404).send("Sorry, can't find that!")
});

app.use(function (req, res, next) {
    res.status(201).send("Missing parameters!")
});


app.use(function (req, res, next) {
    res.status(403).send("Missing access")
});

// API START
client.on("ready", () => {
    console.log(`The API is now online! `)
});

app.listen(PORT, console.log(`the api is listing to`, PORT));

