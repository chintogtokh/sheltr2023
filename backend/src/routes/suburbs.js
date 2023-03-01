import suburbModel from '../models/suburbs';
import { Router } from 'express';

let suburbRouter = Router();

//gets all suburbs
suburbRouter.get('/', (req, res) => {
    var promise = suburbModel.find({});
    promise.then(data => {
        res.send(data);
    })
});

//gets single suburb
suburbRouter.get('/:suburb_shim', (req, res) => {
    var promise = suburbModel.findOne({shim: req.params.suburb_shim});
    promise.then(data => {
        if (data) {
        	res.send(data);
        }
        else {
        	res.status(404).json({
                message: "Suburb doesn't exist"
            });
        }
    })
});

export default suburbRouter;