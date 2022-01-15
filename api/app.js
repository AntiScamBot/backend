// Definitions
const express = require("express"),
    cors = require("cors"),
    app = express();


app.use(cors());

/// OAuth2 
const fetch = require("node-fetch")

require("dotenv").config()
const PORT = process.env.PORT || '80';


// cors Options

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
app.get("/api", cors(corsOptions), (req, res) => {
    const mainpage = (`API for ${name} (${url})`);
    return res.send(mainpage)
});


app.get("/api/v1", cors(corsOptions), (req, res) => {
    const v1page = (`Oops! That looks like, some arguments are missing! soontm comes the Documentation`);
    return res.send(v1page) 
});

/* 
// Not working currently
*/ 
app.get("/api/check/:URL", cors(corsOptions), (req, res) => {
    fetch(req.params.URL).then(URL);
    const response = fetch(URL);

    try {
        fetch(response);
    } catch (error) {
        console.error(error);
    
        const errorBody = error.response.text();
        const check = ({ "status": error.response.text(code)} );
        return res.send(check) 
    }
});


// Error Handling

app.use(function (req, res, next) {
    res.status(404).send("Sorry, can't find that!")
});

app.use(function (req, res, next) {
    res.status(201).send("Missing parameters!")
});

/*
// because it's coming soon
app.use(function (req, res, next) {
    res.status(403).send("Missing access")
});
*/ 

app.listen(PORT, console.log(`the antiscam api is listing to`, PORT));

