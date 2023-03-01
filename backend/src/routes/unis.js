import uniModel from '../models/universities';
import { Router } from 'express';

let uniRouter = Router();

//gets all suburbs
uniRouter.get('/', (req, res) => {
    var promise = uniModel.find({});
    promise.then(data => {
        res.send(data);
    })
});

//gets single suburb
uniRouter.get('/:uni_shim', (req, res) => {
    var promise = uniModel.findOne({shim: req.params.uni_shim});
    promise.then(data => {
        if (data) {
        	res.send(data);
        }
        else {
        	res.status(404).json({
                message: "Uni doesn't exist"
            });
        }
    })
});

export default uniRouter;