# Mixify

A Spotify playlist generating application. Designed with the intent of helping friends and family create designated playlists for gatherings and trips.

Have you ever wanted to create a playlist, mixtape, or CD for your family or friends while going on a trip? One that you could all listen to in the car and enjoy equally together?

Mixify aims to tackle this problem. Using Spotify's API, Mixify takes input playlists from different users. Users can supply any playlist of their choosing, ideally one that will reflect their true music preferences/taste.

Mixify incorporates different playlists and conducts analysis of each playlist's traits, including danceability, tempo, energy, valence, etc. It uses these metrics to formulate a resulting playlist that will equally incorporate each input playlist with the intent that the final product will appeal to all members of the party. The final product will contain songs that each user may recognize from their respective playlists as well as suggesting new ones based on their listening tastes.


An example of Mixify in use:

Here, I have four vastly different playlists. The playlists consist of old school hip-hop music, a blend of jazz, indie/dream rock, and a varied mix of Korean and American modern hip hop, R&B, and pop.

Old School Hip-Hop
<img width="1071" alt="Screen Shot 2021-09-01 at 12 00 14 AM" src="https://user-images.githubusercontent.com/60831327/131610383-e5ac96e5-2331-4ad7-9a10-b4c7b3e18773.png">

Jazz
<img width="1079" alt="Screen Shot 2021-08-31 at 11 59 20 PM" src="https://user-images.githubusercontent.com/60831327/131610417-44610355-3a47-4ac3-84d7-100ae55ba6b8.png">

Indie & Dream Rock
<img width="1074" alt="Screen Shot 2021-08-31 at 11 59 51 PM" src="https://user-images.githubusercontent.com/60831327/131610432-bf4d6c58-66a0-48c5-a0ee-c09c8d75e789.png">

Mix of Korean hip-hop, American hip-hop, R&B, and Pop
<img width="1077" alt="Screen Shot 2021-09-01 at 12 00 27 AM" src="https://user-images.githubusercontent.com/60831327/131610439-4b7eae23-a956-4abd-8866-f6ef64d5816d.png">

These playlists' URLs and our desired features for our resulting playlist is fed into Mixify. After Mixify runs, we get a resulting playlist in our Spotify library:

<img width="1113" alt="Screen Shot 2021-09-01 at 12 02 51 AM" src="https://user-images.githubusercontent.com/60831327/131611043-df387ba3-2539-4323-8457-b65f860d0940.png">

The resulting playlist contains examples of songs that are already in the input playlists as well as new suggestions. We clearly see the influence of each input playlist. The Mixify playlist contains Korean Hip Hop/R&B (All I Wanna Do (K) (Feat. Hoody and Loco), jazz (Herbie Hancock, Snarky Puppy, Mike Stern), old school hip-hop (Dr. Dre), and indie (Mellow Fellow, Jakob). 


 
