import mongoose from 'mongoose';

const UniversitySchema = mongoose.Schema({
    name: {type: String, required: true},
    shim: {type: String},
    coords: {
        lat: Number,
        lng: Number
    }
}, {collection : 'universities'});


UniversitySchema.index({name: 'text'});

export default mongoose.model('University', UniversitySchema);