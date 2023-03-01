import mongoose from 'mongoose';

const SuburbSchema = mongoose.Schema({
    name: {type: String, required: true},
    shim: {type: String, unique: true},
    rating_safety: {type: Number},
    rating_affordability: {type: Number},
    // most_popular_language: {type: String},
    // amenities: {
    // 	bus: Boolean,
    // 	train: Boolean,
    // 	tram: Boolean
    // },
    outlinks: {
    	realestate: String,
    	domain: String
    },
    coords: {
        lat: Number,
        lng: Number
    }
}, {collection : 'suburbs'});

// SuburbSchema.index({name: 'text'});

export default mongoose.model('Suburb', SuburbSchema);