// See https://github.com/dialogflow/dialogflow-fulfillment-nodejs
// for Dialogflow fulfillment library docs, samples, and to report issues
'use strict';
 
const functions = require('firebase-functions');
const {WebhookClient} = require('dialogflow-fulfillment');
const {Card, Suggestion} = require('dialogflow-fulfillment');

 
process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements
 
exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });
  console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
  console.log('Dialogflow Request body: ' + JSON.stringify(request.body));
 
  function welcome(agent) {
    agent.add(`Welcome to my agent!`);
  }
 
  function fallback(agent) {
    agent.add(`I didn't understand`);
    agent.add(`I'm sorry, can you try again?`);
  }


  function hotelsList(agent) {
    agent.add(`Here are the best hotels available:`);
    agent.add(new Card({
      title: `Hotel Haunted `,
      imageUrl: `https://www.traveldaily.com/wp-content/uploads/2017/06/hotel-california-1.jpg`,
      text: `This is the best hotel in the world!`,
      buttonText: `Book`,
      buttonUrl: `http://127.0.0.1:8000/user/Hotel%20Haunted/`
    })
    );

    agent.add( new Card({
      title: `MK Hotel And Resort`,
      imageUrl: `https://www.traveldaily.com/wp-content/uploads/2017/06/hotel-california-1.jpg`,  
      text: `This is the best hotel in the world!`,
      buttonText: `Book`,
      buttonUrl: `http://127.0.0.1:8000/user/MK%20Hotel%20And%20Resort/`
    })
    );

    agent.add( new Card({
      title: `Hotel Royal King`,
      imageUrl: `https://www.traveldaily.com/wp-content/uploads/2017/06/hotel-california-1.jpg`,
      text: `This is the best hotel in the world!`,
      buttonText: `Book`,
      buttonUrl: `http://127.0.0.1:8000/user/Hotel%20Royal%20King/`
    })
    );
    agent.add( new Card({
      title: `Rosewood Resort`,
      imageUrl: `https://www.traveldaily.com/wp-content/uploads/2017/06/hotel-california-1.jpg`,
      text: `This is the best hotel in the world!`,
      buttonText: `Book`,
      buttonUrl: `http://127.0.0.1:8000/user/Rosewood%20Resort/`
    })
    );
    return;
  }

  // Run the proper function handler based on the matched Dialogflow intent name
  let intentMap = new Map();
  intentMap.set('Default Welcome Intent', welcome);
  intentMap.set('Default Fallback Intent', fallback);
  intentMap.set('hotels', hotelsList);
  // intentMap.set('your intent name here', yourFunctionHandler);
  // intentMap.set('your intent name here', googleAssistantHandler);
  agent.handleRequest(intentMap);
});
