import React from 'react';
import { Route, Redirect } from 'react-router-dom';

let PrivateRoute = null;

export default PrivateRoute = ({ component: Component, ...rest }) => (
    <Route {...rest} render={props => (
        localStorage.getItem('user')
            ? <Component {...props} />
            : <Redirect to={{ pathname: '/auth/login', state: { from: props.location } }} />
    )} />
)