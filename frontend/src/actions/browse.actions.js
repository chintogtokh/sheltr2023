import {
    browseConstants
} from '../constants';

export const browseActions = {
    enterPreferences
};

function enterPreferences(data) {

    return { type: browseConstants.ENTERED_PREFERENCES,
            payload: data };

};