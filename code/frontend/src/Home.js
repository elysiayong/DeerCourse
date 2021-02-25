import React from 'react'
import sbp from './assets/search-bar-placeholder.png'
import { ContentCenter } from './components/StyledComponents'

export const Home = () => (
  <ContentCenter>
    <h1 class="main-title"> WELCOME TO DEERCOURSE</h1>
    <h2 class="main-sub">a Course Review Archive by Students at the University of Toronto Mississauga</h2>
    <br></br>
    <img src={sbp} style={{ width: 250 }} alt="Search Bar Placeholder" />
  </ContentCenter>
)