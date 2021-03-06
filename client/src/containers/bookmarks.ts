import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';

import { AppState } from '../constants/types';
import Bookmarks from '../components/bookmarks';

export function mapStateToProps(state: AppState, params: any) {
  return {user: params.match.params.user};
}

export default withRouter(connect(mapStateToProps, {})(Bookmarks));
