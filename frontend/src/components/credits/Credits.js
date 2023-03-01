import React, { Component } from 'react';
import './Credits.css';

class Credits extends Component {

  componentDidMount = function() {
        document.title = "Sheltr | Credits";
    }

    render() {
        return (
        <div>
            <main role="main">
                <div className="container">

                    <h1>Credits</h1>

                    <p>
                      He we are just some of the technologies and data sources we utilised for the application.
                    </p>

                    <h2>Technologies</h2>
                    <ul>
                      <li>ReactJS - front end user interface library</li>
                      <li>Redux - state library</li>
                      <li>MongoDB - database</li>
                      <li>MongooseJS - mongoDB helper library</li>
                      <li>ExpressJS - back end application server (CRUD)</li>
                      <li>Bootstrap v4 - responsive UI library</li>
                    </ul>

                    <h2>Images</h2>
                    <ul>
                    <li>Icons sourced from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> and licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0">CC 3.0 BY</a></li>
                    <li>Suburb Background Images automatically sourced from Google Street View</li>
                    <li>Icons from <a href="https://fontawesome.com">Fontawesome</a></li>
                    <li>Homepage background image of Melbourne &copy; Sharmeen Kaur</li>
                    </ul>

                </div>
            </main>
        </div>
        );
    }
}

export default Credits;
