import React from 'react'
import {SearchBar} from './components/SearchBar';

import sbp from './assets/search-bar-placeholder.png'
import { ContentCenter } from './components/StyledComponents'
import utmLogo from './assets/utm-logo.png'

export const Home = () => (
  <ContentCenter>
    <h1 class="main-title"> WELCOME TO DEERCOURSE 🦌</h1>
    <h2 class="main-sub">a Course Review Archive by Students at the University of Toronto Mississauga</h2>
    <br></br>
    <SearchBar
      showFilter={false}
      collapsible={false}
    />

    <img src={utmLogo} style={{position: "absolute", bottom: 25, right: 25, width: 150}} alt="UTM Logo"/>
  </ContentCenter>
)