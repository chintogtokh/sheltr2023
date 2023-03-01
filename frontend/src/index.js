import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import App from './components/app/App';
// import registerServiceWorker from './registerServiceWorker';
import { unregister } from './registerServiceWorker';
import {stores} from './helpers';
import { PersistGate } from 'redux-persist/integration/react';


ReactDOM.render(
	<Provider store={stores.store}>
	<PersistGate loading={null} persistor={stores.persistor}>
		<App />
	</PersistGate>
	</Provider>,
	document.getElementById('root')
	);
// registerServiceWorker();
unregister();