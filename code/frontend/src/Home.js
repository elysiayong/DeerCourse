import React from 'react'
import sbp from './assets/search-bar-placeholder.png'
import { ContentCenter } from './components/StyledComponents'

export const Home = () => (
  <ContentCenter>
    <h1>DEERCOURSE</h1>
    <br></br>
    <img src={sbp} style={{ width: 250 }} alt="Search Bar Placeholder" />
  </ContentCenter>
)