import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { HashLink } from 'react-router-hash-link';

import './Footer.css';

class Footer extends Component {

  render() {
    return (
        <footer>
          <p>
          <i className="fas fa-code"></i> with <i className="fas fa-beer"></i> in Melbourne by team saladandscrambedeggs &middot; &nbsp;
          <HashLink to="/">home</HashLink>&nbsp;&middot;&nbsp;
          <HashLink smooth to="/#about" scroll={el => el.scrollIntoView({ behavior: "smooth", block: 'start' })}>about</HashLink>
          &nbsp;&middot;&nbsp;
          <Link to="/contact">contact</Link>&nbsp;&middot;&nbsp;
          <Link to="/credits">credits</Link>
          </p>
        </footer>
    );
  }
}

export default Footer;
