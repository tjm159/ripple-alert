import ctypes

import network
import parse as parser
import disk


trellis_url = 'https://rippleneuro.com/support/software-downloads-updates/'


if __name__ == '__main__':
    current_version = disk.read_version() # Current version of trellis

    try:
        # Get web html
        html = network.get_content(trellis_url) 

        # Parse web html to get new version
        new_version = parser.parse_content(html) 
        if current_version != new_version:
            # New version available
            disk.write_version(new_version)
            ctypes.windll.user32.MessageBoxW(
                0, f'Trellis Version {new_version} is available', 
                'New Version', 1)
        else:
            # No new version
            ctypes.windll.user32.MessageBoxW(
                0, f'Trellis Version {current_version} is up to date', 
                'No New Version', 1)

    except (network.NetworkException, parser.ParseException) as e:
        print(e)
        ctypes.windll.user32.MessageBoxW(
            0, 
            'Unable to get the current Trellis version from the Ripple website', 
            e, 1)
