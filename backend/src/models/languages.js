import mongoose from 'mongoose';

const LanguageSchema = mongoose.Schema({
    name: {type: String, required: true},
    shim: {type: String}
}, {collection : 'languages'});


LanguageSchema.index({name: 'text'});

export default mongoose.model('Language', LanguageSchema);