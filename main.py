# Parameters:
# 1. Home Stay: percentage of waking time spent at home
# 2. Screen active frequency: how many times screen was active
# 3. Screen active duration: how long the device's screen was active
# 4. Entropy: Normalized entropy (sum of -p(logp))
# 5. Activity
# 6. Circadian rhythm (consistency of total sleep time)
# 7. Location variance
# 8. Location clusters: utilizes ML algorithm
# 9. Vigorous Activity
# 10. Sleep duration
# 11. Call duration (incoming)
# 12. Call frequency (incoming)
# 13. Call duration (outgoing)
# 14. Call frequency (outgoing)
# 15. Activity Night
# 16. Energy expense
# 17. SMS received

from features.home_stay import *
