/* -------------------- SPEECH FUNCTIONS -------------------- */
function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
}

function listen(callback) {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript.toLowerCase();
        callback(transcript);
    };

    recognition.start();
}

/* -------------------- VOICE MENU -------------------- */
function startVoiceMenu() {
    speak("Welcome! You can say Vote, Take Survey, or View Results. What would you like to do?");

    listen(function(answer) {
        if(answer.includes("vote")) {
            window.location.href = voteURL;
        } else if(answer.includes("survey")) {
            window.location.href = surveyURL;
        } else if(answer.includes("results")) {
            window.location.href = resultsURL;
        } else {
            speak("Sorry, I did not understand. Please say Vote, Take Survey, or View Results.");
            startVoiceMenu();
        }
    });
}

/* -------------------- OPTIONAL: VOICE VOTING -------------------- */
function startVoting() {
    let options = [
        "Accessible Transport",
        "Inclusive Education",
        "Assistive Technology",
        "Healthcare Accessibility",
        "Digital Inclusion"
    ];

    function askVote() {
        speak("Here are the options: " + options.join(", ") + ". Which one do you want to vote for?");

        listen(function(answer) {
            let selected = options.find(opt => answer.includes(opt.toLowerCase()));
            if (selected) {
                let input = document.querySelector(`input[value='${selected}']`);
                if (input) input.checked = true;

                speak("You selected " + selected + ". Do you want to vote for another option? Say yes or no.");

                listen(function(next) {
                    if (next.includes("yes")) {
                        askVote();
                    } else {
                        let form = document.querySelector("form");
                        if (form) form.submit();
                        speak("Your vote has been submitted.");
                    }
                });

            } else {
                speak("I did not understand your choice. Please try again.");
                askVote();
            }
        });
    }

    askVote();
}

/* -------------------- OPTIONAL: VOICE SURVEY -------------------- */
function startSurvey() {
    let questions = document.querySelectorAll(".survey-question");
    let current = 0;

    function askQuestion() {
        if (current >= questions.length) {
            speak("You have completed the survey.");
            return;
        }

        let questionText = questions[current].querySelector("label").innerText;
        speak(questionText);

        listen(function(answer) {
            let options = questions[current].querySelectorAll("input[type='radio']");
            for (let opt of options) {
                if (answer.includes(opt.value.toLowerCase())) {
                    opt.checked = true;
                    speak("You selected " + opt.value);
                }
            }
            current++;
            askQuestion();
        });
    }

    askQuestion();
}

/* -------------------- OPTIONAL: VOICE RESULTS NAVIGATION -------------------- */
function showResults() {
    speak("Here are the current results.");
    speak("Do you want to go back to the welcome page? Say yes or no.");

    listen(function(answer) {
        if (answer.includes("yes")) {
            window.location.href ="{% url 'polls:welcome' %}";
        }
    });
}
