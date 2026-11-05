/* =====================================================================
   TOP CREATION MEDIA — PORTFOLIO DATA
   This is the ONLY file you edit to add work to portfolio.html.
   Copy a template below into the `items` list, fill it in, save. Done.
   A filter tab (Videos, Posters, Websites...) appears automatically as
   soon as it has at least one item.

   FILES: put images in  assets/portfolio/  and refer to them as
          'assets/portfolio/your-file.jpg'  (JPG/PNG/WebP, ~1600px wide).

   ---------------------------------------------------------------------
   TEMPLATE 1 · VIDEO (Google Drive)  — share the file as "Anyone with the link"
   { type: 'video', title: 'Client — campaign name', sub: 'TikTok · 2026',
     driveVideoId: 'PASTE_FILE_ID', driveThumbId: 'PASTE_FILE_ID_OF_THUMBNAIL' },
     (File ID = the long code in the Drive link: drive.google.com/file/d/FILE_ID/view)

   TEMPLATE 2 · VIDEO (YouTube)
   { type: 'video', title: 'Client — campaign name', sub: 'Brand film',
     youtubeId: 'PASTE_VIDEO_ID', image: 'assets/portfolio/cover.jpg' },

   TEMPLATE 3 · POSTER / DESIGN / BRANDING / EVENT  (any image)
   { type: 'poster',   title: 'Client — poster set',   sub: 'Meta ads · 2026', image: 'assets/portfolio/x.jpg' },
   { type: 'branding', title: 'Client — brand identity', sub: 'Logo & guidelines', image: 'assets/portfolio/y.jpg' },
   { type: 'event',    title: 'Client — launch event',  sub: 'Event marketing',  image: 'assets/portfolio/z.jpg' },

   TEMPLATE 4 · RESULTS / DASHBOARD SCREENSHOT
   { type: 'dashboard', title: 'Meta Ads — Client', sub: '3.5x ROAS in 6 weeks', image: 'assets/portfolio/dash.png' },

   TEMPLATE 5 · WEBSITE  (opens the live site in a new tab)
   { type: 'website', title: 'Client website', sub: 'Landing page · built with AI',
     image: 'assets/portfolio/site.jpg', url: 'https://client-site.com' },

   Want a new category (e.g. "Livestream")? Add it to `types` below, then use
   that key as the item's `type`.
   ===================================================================== */

window.TCM_PORTFOLIO = {

  // Order here = order of the filter tabs.
  types: {
    video: 'Videos',
    poster: 'Posters',
    branding: 'Branding',
    website: 'Websites',
    event: 'Events',
    dashboard: 'Results'
  },

  items: [
    // ---- Videos (from the homepage "Selected Work") ----
    { type: 'video', title: 'Short-form video 01', driveThumbId: '1c9Hv7y2g-ToOAJzCW4QK9nXNM19fSQwP', driveVideoId: '1Ty-LZuJjQtZOWxmzonxD0yxITzRKPxSh' },
    { type: 'video', title: 'Short-form video 02', driveThumbId: '1QjgHN5wtQrwgiAICEtYhPXuZpwUILGyT', driveVideoId: '1AIzBUTbEfXdvnCavm7ZvhScY3rUD93Sg' },
    { type: 'video', title: 'Short-form video 03', driveThumbId: '1W9vw0f0eblulrzguykCulbxX9uHAcn7V', driveVideoId: '1SvmH1l3jeTb-LqXkCdXGydT2EMNEV6bP' },
    { type: 'video', title: 'Short-form video 04', driveThumbId: '1V3jWuCXdGTNwYd6aajXcMSctBP1Jw4y9', driveVideoId: '1TOVDmNekJaqW8W3NvhbVr0vW_s3ggaj0' },
    { type: 'video', title: 'Short-form video 05', driveThumbId: '1rsu4a8sG8J_96kOz_EhMVqIIchzZ51ep', driveVideoId: '1sg0BvCMg9dG06Q7GmgJbXZv9gMOhwXL9' },
    { type: 'video', title: 'Short-form video 06', driveThumbId: '15eQtE6Txe7JD3Ql6aCwyf6B0h5MtkEVi', driveVideoId: '1DFUPUcqCcqD_sx37gCxlynC_3prWrF6b' },
    { type: 'video', title: 'Short-form video 07', driveThumbId: '1EA9zExnNeEaPP4CgheXOSIF8jrAtce1O', driveVideoId: '1-c37q5wlcpH_k2srd8gF0RsYuOYSV-N3' },
    { type: 'video', title: 'Short-form video 08', driveThumbId: '1OMMDkhvSRUXvlvKI3isX7wKUvzXvu5Sz', driveVideoId: '1bBietGo_NAcehlakaW-4TuskE0yQNzMn' },
    { type: 'video', title: 'Short-form video 09', driveThumbId: '1ywOaqWZs5Tk5sizyexR6ynGP-pXAG38L', driveVideoId: '1ssZ2tW9awvhQM-wAIOKLQQjuMmMR8REU' },
    { type: 'video', title: 'Short-form video 10', driveThumbId: '16RKEKhPVyUTBk9k3-G_dIK576VMsiYyA', driveVideoId: '1A-hUcTIR8xdjBrnS8Q6QlrgIw9vNYdem' },
    { type: 'video', title: 'Short-form video 11', driveThumbId: '1b5BtjW8rUZT2_7Ns5s_r8FtGt3qZvgsT', driveVideoId: '1aOQy5d4iiKFi25jfMY_fRze_hw-swrkL' },
    { type: 'video', title: 'Short-form video 12', driveThumbId: '1p9azCWx6TpYyaMLSDq-cgcEA26F5OOgM', driveVideoId: '1Fn6Ee_SIf8CzHIgy9DnzrHyn9DINr-tp' },
    { type: 'video', title: 'Short-form video 13', driveThumbId: '12aOLaL3S7-mtPQs7nOO5aqFBA_z6oREe', driveVideoId: '1ToM2cy8Y07o2I9Q0eUl5xN4rFn2s4VPs' },
    { type: 'video', title: 'Short-form video 14', driveThumbId: '1jpNh9M25rCNBnVLvJ5jV0EjkkEBpoVDE', driveVideoId: '1_XELLEYZQag8Maeip_AWVgWaKSQa42qJ' },
    { type: 'video', title: 'Short-form video 15', driveThumbId: '1dhR8VyqeZAsr2RIqWFmXcD6EwO68clKm', driveVideoId: '1vUaPoibc1qNdlP_9PoSRqk7HZcycOA7l' },

    // ---- Results dashboards (from the homepage "Real dashboards. Real numbers.") ----
    { type: 'dashboard', title: 'Google Ecosystem', sub: '+108% organic clicks within 12 months', image: 'assets/google-dashboard.png' },
    { type: 'dashboard', title: 'Meta Ads Mastery', sub: 'Scaling conversions', image: 'assets/meta-dashboard.png' },
    { type: 'dashboard', title: 'TikTok Growth Engine', sub: 'Viral reach & live sales', image: 'assets/tiktok-dashboard.png' }

    // ---- ADD NEW WORK ABOVE THIS LINE (remember the comma after the previous item) ----
  ],

  // Client logos strip at the bottom of the page.
  // TEMPLATE: { name: 'Client name', logo: 'assets/logos/file.png' },
  clients: [
    { name: '3cat', logo: 'assets/logos/3cat.jpeg' },
    { name: 'FnC', logo: 'assets/logos/fnc.jpeg' },
    { name: 'Mobil', logo: 'assets/logos/mobil.jpg' },
    { name: 'TCL', logo: 'assets/logos/tcl.png' },
    { name: 'Nescafé', logo: 'assets/logos/nescafe.jpg' },
    { name: 'NOMI', logo: 'assets/logos/nomi.png' },
    { name: 'TP-Link', logo: 'assets/logos/tp-link.png' },
    { name: 'Royal County of Berkshire Polo Club', logo: 'assets/logos/polo-club.jpeg' },
    { name: 'Golden Tropics', logo: 'assets/logos/golden-tropics.jpeg' },
    { name: 'Joy Paradise', logo: 'assets/logos/joy-paradise.jpg' },
    { name: 'Lau Homecook', logo: 'assets/logos/lau-homecook.png' },
    { name: 'SOFEI', logo: 'assets/logos/sofei.png' },
    { name: 'Haroma Signature', logo: 'assets/logos/haroma.jpg' }
  ]
};
