# Sheltr app

Sheltr - connecting safe homes with new students. The app uses the MERN stack.

## Development

The `nf` package is required. Install using `npm install --global nf`

`npm install` must be run from both the frontend and backend directories.

`nf start` is run from the root.

## Production

Use the `deploy.sh` script as reference. The frontend and backend are built using `npm run build` from both the frontend and backend.

After this, use the server-config scripts to configure Nginx (as reverse proxy for frontend), Node-6000 (as a Systemd daemon for backend), and MongoDB.


## API reference
The API is accessible from the React app.


Getting suburb info:
* `GET` `/api/suburbs/:shim`

Getting university info:
* `GET` `/api/university/:shim`

The shim refers to the suburb name, in shim format. Glen Huntly becomes `glen-huntly`, for example.

Getting ranked suburbs:
* `POST` `/api/ranked_suburbs`. Parameters:
    * `language` (shim format).
    * `uni` (shim format) - Required.
    * `filter` (one of `distance`,`uni`,`safety`,`affordability`) - Defaults to `distance` if not entered.
    * `distance` (a string or numeric value of distance in kilometers) - Required.

Search endpoints:
* `/api/search/universities?q=QUERY`
* `/api/search/languages?q=QUERY`
* `/api/search/suburbs?q=QUERY`