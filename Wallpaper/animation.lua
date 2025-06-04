function get_lines(filename)
    local lines = {}
    -- io.lines returns an iterator, so we need to manually unpack it into an array
    for line in io.lines(filename) do
        lines[#lines+1] = line
    end
    return lines
end

function Initialize()
    os.execute("python HourlyJsonComplier.py")
    hour = os.date("%H")
    start = os.clock()
    frames = get_lines(SKIN:MakePathAbsolute("Resources/frames.txt"))
end

function Update()
    if hour ~= os.date("%H") then
        os.execute("python HourlyJsonComplier.py")
        hour = os.date("%H")
        start = os.clock()
        frames = get_lines(SKIN:MakePathAbsolute("Resources/frames.txt"))
    end

    local n = math.floor(os.clock() - start) + 1
	SKIN:Bang( '!SetWallpaper', frames[n], 'fit')
end