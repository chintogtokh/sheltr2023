import React, { Component } from 'react';
import './VicMap.css';
import { Map, TileLayer, Marker, Popup } from 'react-leaflet';

const inner = [[49.505, -2.09], [53.505, 2.09]];
const outer = [[50.505, -29.09], [52.505, 29.09]];

class VicMap extends Component {

    state = {
        bounds: outer,
        lat: -37.4207738,
        lng: 144.8265929,
        zoom: 7
    }

    onClickInner = () => {
      this.setState({ bounds: inner })
    }

    onClickOuter = () => {
      this.setState({ bounds: outer })
    }

    render() {

        const position = [this.state.lat, this.state.lng]

        return (
        <div>
            <main role="main">
                <div className="container">

                    <h1>Mappa mundi</h1>

                        <Map style={{'height':500+'px','width':100+'%'}} center={position} zoom={this.state.zoom}>
                            <TileLayer
                              attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
                              url="https://{s}.tiles.mapbox.com/v3/mapbox.blue-marble-topo-jul/{z}/{x}/{y}.png"
                            />
                        <Marker position={position}>
                          <Popup>
                            <span>
                              A pretty CSS3 popup. <br /> Easily customizable.
                            </span>
                          </Popup>
                        </Marker>
                        </Map>
                </div>
            </main>
        </div>
        );
    }
}

export default VicMap;
