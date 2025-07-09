const timestamp = new Date().toISOString().replace(/[-:T]/g, '').slice(0, 12); // e.g., 202507091610

module.exports = {
  output: 'export',
  distDir: 'out-' + timestamp, // dynamically name folder
  trailingSlash: true,
};
