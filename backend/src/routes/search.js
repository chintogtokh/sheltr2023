import universityModel from '../models/universities';
import languageModel from '../models/languages';
import suburbModel from '../models/suburbs';

import {
    Router
} from 'express';

let searchRouter = Router();

searchRouter.get('/universities', (req, res) => {

    let searchText = req.query.q;

    var srches = searchText.split(" ");

    var query = [];

    for (var i = 0; i < srches.length; i++) {
        query.push({'name': {'$regex': srches[i], '$options': 'i'}});
    }

    universityModel.find({'$and': query}).limit(10).exec(function(err, docs) {
        res.send(docs)
    });;

    // universityModel.find({ $text: { $search: searchText, $language: 'english' } } ).limit(10).exec(function(err, docs) {
    //     res.send(docs)
    // });

});

searchRouter.get('/languages', (req, res) => {

    let searchText = req.query.q;


    var srches = searchText.split(" ");

    var query = [];

    for (var i = 0; i < srches.length; i++) {
        query.push({'name': {'$regex': srches[i], '$options': 'i'}});
    }

    languageModel.find({'$and': query}).limit(10).exec(function(err, docs) {
        res.send(docs)
    });

});



searchRouter.get('/suburbs', (req, res) => {

    let searchText = req.query.q;
    // console.log(req.query);

    // suburbModel.find({'name': {'$regex': searchText, '$options': 'i'}},"name shim").limit(10).exec(function(err, docs) {
    //     res.send(docs)
    // });;

    var srches = searchText.split(" ");

    var query = [];

    for (var i = 0; i < srches.length; i++) {
        query.push({'name': {'$regex': srches[i], '$options': 'i'}});
    }

    suburbModel.find({'$and': query}).limit(10).exec(function(err, docs) {
        res.send(docs)
    });

});

export default searchRouter;