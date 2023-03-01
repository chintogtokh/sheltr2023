import {browseConstants} from '../constants';

export function browse(state = {}, action) {
	switch(action.type){
		case browseConstants.ENTERED_PREFERENCES:
			return action.payload;
		default:
			return state;
	}
}