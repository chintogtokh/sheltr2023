import React, { Component } from 'react';
import './Navbar.css';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import full_logo_inverse from '../../files/full_logo_inverse.svg';

class Navbar extends Component {

  render() {
    const { user, loggedIn } = this.props;
    return (
      <nav className="navbar navbar-expand-md navbar-dark">
        <Link to="/" className="navbar-brand"><img src={full_logo_inverse} alt="Sheltr logo"/></Link>
          {false && !loggedIn &&
            <ul className="navbar-nav ml-md-auto">
                <li className="nav-item">
                  <Link to="/auth/login" className="nav-link">login</Link>
                </li>
                <li className="nav-item">
                  <Link to="/auth/register" className="nav-link">register</Link>
                </li>
            </ul>
          }
          {false && loggedIn &&
            <ul className="navbar-nav ml-md-auto">
                <li className="nav-item">
                  <Link to="/auth/logout" className="nav-link">logout ({user.username})</Link>
                </li>
            </ul>
          }
      </nav>
    );
  }
}

function mapStateToProps(state) {
    let { loggedIn, user } = state.authentication;
    try{
      user = user.user;
    }
    catch(e){
      //dont care for now
    }
    return {
        loggedIn, user
    };
}

export default connect(mapStateToProps)(Navbar);
