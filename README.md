## Theta Fire

Theta.tv app brought to your Amazon Fire TV device.

## Inspiration
With the recent launch of THETA.tv app on the Android TV platform we were excited to see Theta-powered channels available and the ability to earn Theta Fuel on 10-foot devices. We were inspired to extend the Theta ecosystem to our favorite streaming platform, the widely popular Amazon Fire TV, so we could integrate Alexa voice controls to make browsing and searching a breeze.
## What it does
Theta Fire brings decentralized peer-to-peer video delivery to the Fire TV platform allowing integration with Amazon Alexa voice controls. Viewers can browse streams sorted by category, create a watch list or search for specific streams by speaking directly into a Fire TV remote.
## How I built it
Theta Fire is an Android based streaming app build in Java, which integrates the **Theta Protocol Delivery Android SDK Library** to do distributed P2P streaming on the the Theta network
## Challenges I ran into
We originally built the app using the Amazon media player which would not run after implementing the Theta Delivery SDK despite utilizing the ExoPlayer for playback. We worked hard to replace it with a standard Exoplayer to allow peer to peer video sharing.
## Accomplishments that I'm proud of
We can successfully stream Theta.tv on Amazon Fire TV devices.

## What's next for Theta Fire
* Release open source
* Add live updates to the video stream view (vs. just the initial request).
* Add payment options.

