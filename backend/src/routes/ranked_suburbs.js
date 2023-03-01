import suburbModel from '../models/suburbs';
import {
    Router
} from 'express';

let rankedSuburbRouter = Router();

rankedSuburbRouter.post('/', (req, res) => {
    // res.send([1, 2, 3]);
    const preferences = req.body;

    for(var key in preferences){
        if (preferences[key]==null){
            delete preferences[key];
        }
    }
    //var promise = suburbModel.aggregate({ $mul: { rating_safety: 1.25} },"rating_safety rating_affordability");

    var language = (typeof preferences.language !== "undefined")? preferences.language :null;
    var uni = (typeof preferences.uni !== "undefined")?preferences.uni:null;
    var filter = (typeof preferences.filter !== "undefined")?preferences.filter:null;
    var distance = (typeof preferences.distance !== "undefined")?preferences.distance:null;

    if(!uni && !distance){
        res.send([]);
        return;
    }


    var query = [{
        "$match": {}
    },{
        $project: {
            name: true,
            shim: true,
            ["stats.suburb-residents"]: true,
            rating_affordability: true,
            coords: true,
            ["university_distances."+uni]: true,
            rating_safety: true,
            ["language." + language]: true,
            "stats.price-range-rank": true,
            "stats.suburb-town-name-2016-adjusted-crime-rank" : true,
            "stats.suburb-most-common-expense-tier": true,
        }
    }];

    //distance
    query[0]['$match']["university_distances."+uni+".number"] = { "$exists": true, "$lt": parseFloat(distance) };

    //remove population zero
    query[0]['$match']["stats.suburb-residents.number"] = { "$exists": true, "$ne": 0 };

    //coz data
    query[0]['$match']["stats.suburb-most-common-expense-tier.number"] = { "$exists": true, "$ne": "As at 2016, there are no rental properties listed in this area." };


    var sorter = "";
    var sorter_bool = 1;
    switch(filter){
        case "affordability":
            sorter = "stats.price-range-rank.number";
            sorter_bool = -1;
            break;
        case "safety":
            sorter = "stats.suburb-town-name-2016-adjusted-crime-rank.number";
            sorter_bool = -1;
            break;
        case "language":
            sorter = "language."+language;
            sorter_bool = -1;
            query[0]['$match']["language." + language] = { "$exists": true, "$ne": 0 };
            break;
        case "distance":
        default:
            sorter = "university_distances."+uni+".number";
            sorter_bool = 1;
    }

    suburbModel.aggregate(query).sort({
        [sorter]: sorter_bool
    }).limit(100).exec(function(err, docs) {
        if(typeof docs==="undefined"){
            res.send([]);
        }
        else{
            res.send(docs);
        }
    });;

});

export default rankedSuburbRouter;