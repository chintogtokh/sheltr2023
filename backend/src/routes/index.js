import { version } from '../../package.json';
import { Router } from 'express';
import suburbs from './suburbs';
import ranked_suburbs from './ranked_suburbs';
import search from './search';
import unis from './unis';

let api = Router();

// api.use('/api/cars', passport.authenticate('jwt', {session: false}), cars);
api.use('/api/suburbs', suburbs);
api.use('/api/ranked_suburbs', ranked_suburbs);
api.use('/api/university', unis);

api.use('/api/search', search);

// perhaps expose some API metadata at the root
api.get('/api', (req, res) => {
	res.json({ version });
});

api.get('*', function(req, res) {
    res.redirect('/');
});

export default api;