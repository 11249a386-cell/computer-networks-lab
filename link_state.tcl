set ns [new Simulator]
set nr [open thro.tr w]
$ns trace-all $nr
set nf [open thro.nam w]
$ns namtrace-all $nf

proc finish {} {
    global ns nr nf
    $ns flush-trace
    close $nf
    close $nr
    exec nam thro.nam &
    exit 0
}

for {set i 0} {$i < 12} {incr i} { set n($i) [$ns node] }
for {set i 0} {$i < 8} {incr i} {
    $ns duplex-link $n($i) $n([expr {$i+1}]) 1Mb 10ms DropTail
}
$ns duplex-link $n(0) $n(8) 1Mb 10ms DropTail
$ns duplex-link $n(1) $n(10) 1Mb 10ms DropTail
$ns duplex-link $n(0) $n(9) 1Mb 10ms DropTail
$ns duplex-link $n(9) $n(11) 1Mb 10ms DropTail
$ns duplex-link $n(10) $n(11) 1Mb 10ms DropTail
$ns duplex-link $n(11) $n(5) 1Mb 10ms DropTail

foreach pair {{0 1} {1 5}} {
    lassign $pair src dst
    set udp($src) [new Agent/UDP]
    $ns attach-agent $n($src) $udp($src)
    set cbr($src) [new Application/Traffic/CBR]
    $cbr($src) set packetSize_ 500
    $cbr($src) set interval_ 0.005
    $cbr($src) attach-agent $udp($src)
    set sink($src) [new Agent/Null]
    $ns attach-agent $n(5) $sink($src)
    $ns connect $udp($src) $sink($src)
    $udp($src) set fid_ [expr {$src + 1}]
}
$ns rtproto LS
$ns rtmodel-at 10.0 down $n(11) $n(5)
$ns rtmodel-at 15.0 down $n(7) $n(6)
$ns rtmodel-at 20.0 up $n(7) $n(6)
$ns rtmodel-at 30.0 up $n(11) $n(5)
$ns color 1 Red
$ns color 2 Green
$ns at 1.0 "$cbr(0) start"
$ns at 2.0 "$cbr(1) start"
$ns at 45.0 "finish"
$ns run
