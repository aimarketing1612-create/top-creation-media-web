/* =====================================================================
   TOP CREATION MEDIA — VIDEOS & TESTIMONIALS
   The ONLY file you edit to add your intro videos and client reviews.

   ---------------------------------------------------------------------
   1) VIDEOS  (16:9; the three AI Video samples are 9:16 vertical). Fill in ONE of the three options per video:
        mp4:       '/assets/video/home.mp4'   BEST: a file you upload to deploy/assets/video/
                                              (H.264 MP4, 1080p, under ~10 MB)
        youtubeId: 'dQw4w9WgXcQ'    the code after watch?v= in a YouTube link
        driveId:   'FILE_ID'        Google Drive (click-to-play only, cannot autoplay)
      Optional: poster: '/assets/video/home-cover.jpg'  (cover image shown while loading)

      VIDEO TOO BIG? Shrink it first: bash tools/compress_video.sh <your-video.mp4> home
      (needs ffmpeg; writes the MP4 and a cover image into deploy/assets/video/).
      Or upload it to YouTube as Unlisted and paste the code into youtubeId.

      AUTOPLAY: MP4 and YouTube videos play automatically when the visitor
      reaches them, MUTED (browsers block autoplay with sound). A "Sound on"
      button lets visitors turn the sound on. To turn autoplay off for one
      video, add  autoplay: false
      Leave all empty ('') and the page shows a "Video coming soon" frame.

   2) TESTIMONIALS. Only add REAL client reviews (with permission).
      The section stays hidden until at least one is added. Template:
        { name: 'Jane Tan', role: 'Founder, Brand Name', quote: 'What they said...',
          photo: '/assets/bts/jane.jpg' },     <- photo is optional
   ===================================================================== */

window.TCM_MEDIA = {
  videos: {
    home:         { youtubeId: '', driveId: '', mp4: '', poster: '' },  // Home page intro
    social:       { youtubeId: '', driveId: '', mp4: '', poster: '' },  // Social Media page intro
    services:     { youtubeId: '', driveId: '', mp4: '', poster: '' },  // Done-For-You page
    academy:      { youtubeId: '', driveId: '', mp4: '', poster: '' },  // Marketing Academy page
    ai:           { youtubeId: '', driveId: '', mp4: '', poster: '' },  // AI Classes intro
    'scan-buddy': { youtubeId: '', driveId: '', mp4: '', poster: '' },  // Scan Buddy demo
    'ai-video':   { youtubeId: '', driveId: '', mp4: '', poster: '' },  // AI Video demo
    // AI Video page: three vertical (9:16) sample videos
    'ai-video-1': { youtubeId: '', driveId: '', mp4: '', poster: '' },
    'ai-video-2': { youtubeId: '', driveId: '', mp4: '', poster: '' },
    'ai-video-3': { youtubeId: '', driveId: '', mp4: '', poster: '' },
  },

  testimonials: [
    // { name: '', role: '', quote: '', photo: '' },
  ],
};
