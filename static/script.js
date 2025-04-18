

document.getElementById('recordButton').addEventListener('click', function(e) {
  recordVoice();
    const button = document.querySelector("#recordButton");
    button.classList.add("animate");
    setTimeout(() => {
        button.classList.remove("animate");
    }, 600);
});



async function recordVoice() {
  try {
      console.log("listening")
      const recognition = new webkitSpeechRecognition() //|| new SpeechRecognition();
      recognition.lang = 'en-us';
      recognition.start();
    
        recognition.onresult = async (event) => {
            const voice_command = event.results[0][0].transcript;
            console.log('Voice command:', voice_command);
            console.log("listening stopped")

            
            // Send the voice command to Flask backend
            document.getElementById('output').textContent = voice_command;
            const response = await sendVoiceCommand(voice_command);
            
        };
  
        recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
        };
        
  } catch (error) {
      console.error('Error initializing speech recognition:', error);
  }
}


async function sendVoiceCommand(voice_command) {
  try {
      const response = await fetch('/process_voice_command', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ voice_command })
      });
      document.get
      if (!response.ok) {
          throw new Error('Failed to fetch response from server');
      }

      const responseData = await response.json();
      const serverResponse = responseData.response;

      // Log the response to the console
      console.log('Server response:', serverResponse);

      // Display the response on the webpage
      document.getElementById('response').textContent = serverResponse;

      return responseData.response;
  } catch (error) {
      console.error('Error sending voice command:', error);
      return 'Error: Failed to process voice command';
  }
}