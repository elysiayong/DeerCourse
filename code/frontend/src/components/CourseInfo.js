import axios from "axios";
import React, { useEffect, useState } from "react";
import { CourseComponent } from "./CourseComponent";
import "../App.css";

// Inspired by https://codewithnico.com/react-wait-axios-to-render/
// Component responsible for loading course data
export const CourseInfo = (courseName) => {
  const [loading, setLoading] = useState(true);
  const [courseInfo, setCourseInfo] = useState(false);

  // Making use of useEffect hook to fetch and set course data
  useEffect(() => {
    // Uses proxy to access the query DB
    axios
      .get("/courses/" + courseName)
      .then(function (response) {
        // Response received, check status code
        if (
          response &&
          response.status === 200 &&
          response.hasOwnProperty("data") // potentially unnecessary
        ) {
          setCourseInfo(response.data);
        }
        setLoading(false);
      })
      .catch(function (error) {
        // Error occurred when receiving data
        console.log(error);
      })
      .finally(function () {
        // set loading to false
        setLoading(false);
      });
  }, [courseName]); // Rerun only if courseName changes

  if (loading) {
    // Initial render, course data hasn't loaded
    return <h1>LOADING...</h1>;
  }

  if (courseInfo) {
    // Second render course data has loaded
    // Call to subcomponent to render data
    return <CourseComponent courseName={courseName} courseInfo={courseInfo} />;
  } else {
    // Course info failed to load
    return false;
  }
};
