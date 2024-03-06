function makeCall() {
  const name = document.getElementById("name").value;
  const phoneNumber = document.getElementById("phoneNumber").value;
  const jobTitle = document.getElementById("jobTitle").value;
  const jobLocation = document.getElementById("jobLocation").value;
  const hourlyRate = document.getElementById("hourlyRate").value;
  const jobType = document.getElementById("jobType").value;
  const remote = document.getElementById("remote").value;
  const requiredSkills = document.getElementById("requiredSkills").value;
  const recruiterName = document.getElementById("recruiterName").value;
  const recruiterPhone = document.getElementById("recruiterPhone").value;
  const recruiterEmail = document.getElementById("recruiterEmail").value;

  const modelId = "1707142827149x519497455730688000";

  const options = {
    method: "POST",
    headers: {
      accept: "application/json",
      "content-type": "application/json",
      Authorization: "Bearer 1704476529550x370244089367633100",
    },
    body: JSON.stringify({
      model: modelId,
      phone: phoneNumber,
      name: name,
      custom_variables: [
        `job_title: ${jobTitle}`,
        `job_location: ${jobLocation}`,
        `hourly_rate: ${hourlyRate}`,
        `job_type: ${jobType}`,
        `remote: ${remote}`,
        `required_skills: ${requiredSkills}`,
        `recruiter_name: ${recruiterName}`,
        `recruiter_phone: ${recruiterPhone}`,
        `recruiter_email: ${recruiterEmail}`,
      ],
    }),
  };

  const apiUrl = "/api/call"; // Adjust the route according to your Flask app

  fetch(apiUrl, options)
    .then((response) => response.json())
    .then((data) => {
      displayOutput(data);
    })
    .catch((error) => {
      console.error("Error making API call:", error);
      displayOutput({ status: "error", response: error.message });
    });
}

function displayOutput(data) {
  const outputDiv = document.getElementById("output");
  outputDiv.innerHTML = `
              <p>Status: ${data.status}</p>
              <p>Response: ${JSON.stringify(data.response)}</p>
          `;
}

function makeMultipleCalls() {
  const formData = new FormData();
  const fileInput = document.getElementById("file");
  formData.append("file", fileInput.files[0]);

  const customVariables = {
    jobTitle: document.getElementById("jobTitle").value,
    jobLocation: document.getElementById("jobLocation").value,
    hourlyRate: document.getElementById("hourlyRate").value,
    jobType: document.getElementById("jobType").value,
    remote: document.getElementById("remote").value,
    requiredSkills: document.getElementById("requiredSkills").value,
    recruiterName: document.getElementById("recruiterName").value,
    recruiterPhone: document.getElementById("recruiterPhone").value,
    recruiterEmail: document.getElementById("recruiterEmail").value,
  };

  formData.append("custom_variables", JSON.stringify(customVariables));

  fetch("/api/make-multiple-calls", {
    method: "POST",
    body: formData,
    headers: {
      Accept: "application/json", // Specify the accepted response content type
      "Content-Type": "multipart/form-data", // Specify the content type of the request
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      // Handle response as needed
    })
    .catch((error) => console.error("Error making multiple calls:", error));
}

//Synthflow
function makeCallSynthflow() {
  const name = document.getElementById("name").value;
  const phoneNumber = document.getElementById("phoneNumber").value;
  const jobTitle = document.getElementById("jobTitle").value;
  const jobLocation = document.getElementById("jobLocation").value;
  const hourlyRate = document.getElementById("hourlyRate").value;
  const jobType = document.getElementById("jobType").value;
  const remote = document.getElementById("remote").value;
  const requiredSkills = document.getElementById("requiredSkills").value;
  const recruiterName = document.getElementById("recruiterName").value;
  const recruiterPhone = document.getElementById("recruiterPhone").value;
  const recruiterEmail = document.getElementById("recruiterEmail").value;

  const modelId = "1707142827149x519497455730688000";

  const options = {
    method: "POST",
    headers: {
      accept: "application/json",
      "content-type": "application/json",
      Authorization: "Bearer 1704476529550x370244089367633100",
    },
    body: JSON.stringify({
      model: modelId,
      phone: phoneNumber,
      name: name,
      custom_variables: [
        `job_title: ${jobTitle}`,
        `job_location: ${jobLocation}`,
        `hourly_rate: ${hourlyRate}`,
        `job_type: ${jobType}`,
        `remote: ${remote}`,
        `required_skills: ${requiredSkills}`,
        `recruiter_name: ${recruiterName}`,
        `recruiter_phone: ${recruiterPhone}`,
        `recruiter_email: ${recruiterEmail}`,
      ],
    }),
  };

  const apiUrl = "/api/call"; // Adjust the route according to your Flask app

  fetch(apiUrl, options)
    .then((response) => response.json())
    .then((data) => {
      displayOutput(data);
    })
    .catch((error) => {
      console.error("Error making API call:", error);
      displayOutput({ status: "error", response: error.message });
    });
}

function displayOutput(data) {
  const outputDiv = document.getElementById("output");
  outputDiv.innerHTML = `
              <p>Status: ${data.status}</p>
              <p>Response: ${JSON.stringify(data.response)}</p>
          `;
}

function makeCallVodex() {
  const name = document.getElementById("name").value;
  const phoneNumber = document.getElementById("phoneNumber").value;
  const jobTitle = document.getElementById("jobTitle").value;
  const jobLocation = document.getElementById("jobLocation").value;
  const hourlyRate = document.getElementById("hourlyRate").value;
  const jobType = document.getElementById("jobType").value;
  const remote = document.getElementById("remote").value;
  const requiredSkills = document.getElementById("requiredSkills").value;
  const recruiterName = document.getElementById("recruiterName").value;
  const recruiterPhone = document.getElementById("recruiterPhone").value;
  const recruiterEmail = document.getElementById("recruiterEmail").value;

  const projectId = "65c644d755dada1fbe061f73";

  const options = {
    method: "POST",
    headers: {
      accept: "application/json",
      "content-type": "application/json",
      Authorization: "f422b7cc-85ef-421d-b487-fbe9c6ab1a46",
    },
    body: JSON.stringify({
      firstName: name,
      lastName: "Sai",
      phone: phoneNumber,
      job_title: jobTitle,
      job_location: jobLocation,
      hourly_rate: hourlyRate,
      job_type: jobType,
      remote: remote,
      required_skills: requiredSkills,
      recruiter_name: recruiterName,
      recruiter_phone: recruiterPhone,
      recruiter_email: recruiterEmail,
      projectId: projectId,
    }),
  };
  console.log();
  const apiUrl = "/api/vodexcall"; // Adjust the route according to your Flask app

  fetch(apiUrl, options)
    .then((response) => {
      // Check if the response status is successful
      if (response.ok) {
        // If the response is successful, parse the JSON response
        return response.json();
      } else {
        // If the response is not successful, throw an error
        throw new Error("Request failed: " + response.statusText);
      }
    })
    .then((data) => {
      console.log(data); // Log the response data to the console

      // Handle the successful response
      if (data.userId && data.token) {
        // If the response contains userId and token
        displayOutput({ status: "success", response: data });
      } else {
        // If the response doesn't match the expected schema
        throw new Error("Invalid response format");
      }
    })
    .catch((error) => {
      // Handle errors
      console.error("Error making API call:", error);
      // displayOutput({ status: "error", response: error.message });
    });
}
