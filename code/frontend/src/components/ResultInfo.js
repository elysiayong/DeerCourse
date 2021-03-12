import axios from "axios";
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

export const ResultInfo = (props) => {
  const { code, level, duration } = props;
  const [loading, setLoading] = useState(true);
  const [results, setResults] = useState([]);

  useEffect(() => {
    // Forming request body
    var body = {};
    body["code"] = code;
    if (level) body["level"] = level;
    if (duration) body["duration"] = duration;

    axios
      .post("http://localhost:8080/courses/search", body)
      .then(function (response) {
        if (response.status === 200 && response.hasOwnProperty("data")) {
          // Request was successful
          console.log("Request successful");
          setResults(response.data);
        }
      })
      .catch(function (error) {
        // Request failed
        console.log(error);
        setResults([]);
      })
      .finally(function () {
        // Change loading state to render results
        setLoading(false);
      });
  }, [code, level, duration]); // Rerun only if these variables change changes

  if (loading) {
    return <h1>LOADING...</h1>;
  }

  if (results.length) {
    return (
      <React.Fragment>
        <h1>Results</h1>
        <p>
          {results.map((course) => (
            <React.Fragment key={course.code}>
              <Link to={"/course/" + course.code}>{course.code}</Link>
              <br />
            </React.Fragment>
          ))}
        </p>
      </React.Fragment>
    );
  } else {
    return <h1>NO RESULTS</h1>;
  }
};
