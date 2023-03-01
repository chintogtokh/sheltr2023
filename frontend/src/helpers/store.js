import { createStore, applyMiddleware, compose } from 'redux';
import { persistStore, persistReducer } from 'redux-persist';
import thunkMiddleware from 'redux-thunk';
import rootReducer from '../reducers';
import storage from 'redux-persist/lib/storage';
import autoMergeLevel2 from 'redux-persist/lib/stateReconciler/autoMergeLevel2';

// const loggerMiddleware = createLogger();

const persistConfig = {
  key: 'root',
  storage,
  stateReconciler: autoMergeLevel2,
};

const persistedReducer = persistReducer(persistConfig, rootReducer);

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

let store = createStore(persistedReducer, composeEnhancers(
	applyMiddleware(
        	thunkMiddleware
    	),
	));

let persistor = persistStore(store);

export const stores = {
  store, persistor
}