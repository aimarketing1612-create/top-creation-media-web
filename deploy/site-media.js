/* =====================================================================
   TOP CREATION MEDIA — VIDEOS & TESTIMONIALS
   The ONLY file you edit to add your intro videos and client reviews.

   ---------------------------------------------------------------------
   1) VIDEOS  (16:9). Fill in ONE of the three options per video:
        youtubeId: 'dQw4w9WgXcQ'    the code after watch?v= in a YouTube link
        driveId:   'FILE_ID'        Google Drive: share as "Anyone with the link",
                                    code from drive.google.com/file/d/FILE_ID/view
        mp4:       '/assets/video/home.mp4'   a file you upload to the site
      Optional: poster: '/assets/video/home-cover.jpg'  (cover image)
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
  },

  testimonials: [
    // { name: '', role: '', quote: '', photo: '' },
  ],
};
