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
      reaches them, MUTED (browsers block autoplay with sound). Visitors tap
      the video or its "Tap for sound" label to hear it; only one plays sound at a time. To turn autoplay off for one
      video, add  autoplay: false
      Leave all empty ('') and that video frame is left out of the page (run python3 tools/build_site.py after changing this file).

   2) TESTIMONIALS. Only add REAL client reviews (with permission).
      The section stays hidden until at least one is added. Template:
        { name: 'Jane Tan', role: 'Founder, Brand Name', quote: 'What they said...',
          photo: '/assets/bts/jane.jpg' },     <- photo is optional
   ===================================================================== */

window.TCM_MEDIA = {
  videos: {
    home:         { youtubeId: '', driveId: '', mp4: '/assets/video/home.mp4', poster: '/assets/video/home-cover.jpg' },  // Home page intro
    social:       { youtubeId: '', driveId: '', mp4: '', poster: '' },  // Social Media page intro
    services:     { youtubeId: '', driveId: '', mp4: '', poster: '' },  // Done-For-You page
    academy:      { youtubeId: '', driveId: '', mp4: '/assets/video/academy.mp4', poster: '/assets/video/academy-cover.jpg' },  // Marketing Academy page
    ai:           { youtubeId: '', driveId: '', mp4: '/assets/video/ai.mp4', poster: '/assets/video/ai-cover.jpg' },  // AI Classes intro
    'scan-buddy': { youtubeId: '', driveId: '', mp4: '', poster: '' },  // Scan Buddy demo
    'ai-video':   { youtubeId: '', driveId: '', mp4: '', poster: '' },  // AI Video demo
    // Home page: team intro videos (with BGM; plays muted, visitors tap "Sound on")
    'team-emma':   { youtubeId: '', driveId: '', mp4: '/assets/video/team-emma.mp4', poster: '/assets/video/team-emma-cover.jpg' },
    'team-jess':   { youtubeId: '', driveId: '', mp4: '/assets/video/team-jess.mp4', poster: '/assets/video/team-jess-cover.jpg' },
    'team-mac':    { youtubeId: '', driveId: '', mp4: '/assets/video/team-mac.mp4', poster: '/assets/video/team-mac-cover.jpg' },
    'team-marcus': { youtubeId: '', driveId: '', mp4: '/assets/video/team-marcus.mp4', poster: '/assets/video/team-marcus-cover.jpg' },
    // AI Academy page: five vertical (9:16) samples: 1 UGC ad, 2 AI short film, 4 outfit & background swap, 5 product footage, 6 B-roll
    'ai-video-1': { youtubeId: '', driveId: '', mp4: '/assets/video/ai-video-1.mp4', poster: '/assets/video/ai-video-1-cover.jpg' },
    'ai-video-2': { youtubeId: '', driveId: '', mp4: '/assets/video/ai-video-2.mp4', poster: '/assets/video/ai-video-2-cover.jpg' },
    'ai-video-4': { youtubeId: '', driveId: '', mp4: '/assets/video/ai-video-4.mp4', poster: '/assets/video/ai-video-4-cover.jpg' },
    'ai-video-5': { youtubeId: '', driveId: '', mp4: '/assets/video/ai-video-5.mp4', poster: '/assets/video/ai-video-5-cover.jpg' },
    'ai-video-6': { youtubeId: '', driveId: '', mp4: '/assets/video/ai-video-6.mp4', poster: '/assets/video/ai-video-6-cover.jpg' },
  },

  testimonials: [
    // { name: '', role: '', quote: '', photo: '' },
  ],
};
