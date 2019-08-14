import wavedrom
from wavedrom import bitfield
import copy

opt = bitfield.Options(bits=8, lanes=1)
reg = [{"name": 'Frequency[11:8]', "bits": 3},
       {"name": '', "bits": 3},
       {"name": 'Continuous', "bits": 1},
       {"name": 'Start', "bits": 1}]
reg = bitfield.BitField().render(reg, opt)
reg.saveas("voice1.svg")

bootloader ={ "signal": [
    { "name": "Clock",        "wave": "p.", "period": 4  },
    { "name": "Address[:16]", "wave": "x=.=", "data": "0x0100", "period": 2, "phase": 0.5 },
    { "name": "Data[:8]",     "wave": "z.=z", "data": "'o'", "period": 2, "phase": 0.5 },
], "config": {"skin": "narrow"}}
svg = wavedrom.WaveDrom().render_waveform(0, bootloader, [])
# Patch the lane translation to leave less padding.
svg.elements[1].elements[0].attribs["transform"] = ""
svg.elements[1].elements[0].translate(100, 0)
svg.saveas("bootloader.svg")

source ={ "signal": [
    { "name": "Clock",        "wave": "p.......", "period": 4  },
    { "name": "Address[:16]", "wave": "x=.=.=.=.=.x.=.", "data": "0x0100 0x0101 0x0102 0x0103 0x0104", "period": 2, "phase": 0.5 },
    { "name": "Data[:8]",     "wave": "z.3z=z3z=z3z...", "data": "0x0e 0x87 0x3e 0x14 0xe2", "period": 2, "phase": 0.5 },
], "config": {"skin": "narrow"}}

width = None
for i, subset in reversed(list(enumerate([3, 5, 6, -1]))):
    subset_source = copy.deepcopy(source)
    for signal in subset_source["signal"]:
        end = subset
        if end != -1 and signal["wave"][0] not in "pPnN":
            end *= 2
        signal["wave"] = signal["wave"][:end]
    if subset > 0:
        subset_source["signal"][1]["data"] = " ".join(subset_source["signal"][1]["data"].split()[:subset-1])
    svg = wavedrom.WaveDrom().render_waveform(0, subset_source, [])
    if width:
        svg["width"] = width
    else:
        width = svg["width"]
    # Patch the lane translation to leave less padding.
    svg.elements[1].elements[0].attribs["transform"] = ""
    svg.elements[1].elements[0].translate(100, 0)
    svg.saveas("demo{}.svg".format(i))
