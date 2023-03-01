import React, { Component } from 'react';
import './Contact.css';

class Contact extends Component {

    componentDidMount = function() {
        document.title = "Sheltr | Contact";
    }

    render() {
        return (
        <div>
            <main role="main">
                <div className="container">
                    <h1>Contact us</h1>
                    <div>Hi there, we're four students at Monash Uni. We are:</div>
                    <ul>
                      <li>Chintogtokh Batbold</li>
                      <li>James Furnell</li>
                      <li>Sharmeen Kaur</li>
                      <li>Wanping Yang</li>
                    </ul>

                    <div>
                      You can give us a shout at <code style={{color: 'black', fontWeight: 'bold'}}>saladandscrambledeggs [AT] gmail [DOT] [COM]</code>
                    </div>
                </div>
            </main>
        </div>
        );
    }
}

export default Contact;
