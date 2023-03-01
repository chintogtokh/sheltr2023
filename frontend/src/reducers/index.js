import { combineReducers } from 'redux';
import { authentication } from './authentication.reducer';
import { registration } from './registration.reducer';
import { users } from './users.reducer';
import { alert } from './alert.reducer';
import { suburb } from './suburb.reducer';
import { browse } from './browse.reducer';

const rootReducer = combineReducers({
  authentication,
  registration,
  users,
  alert,
  suburb,
  browse
});

export default rootReducer;