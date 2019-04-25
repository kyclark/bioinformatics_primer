#!/usr/bin/env perl6

sub MAIN (Str :$in-dir! where *.IO.d, Str :$out-dir!, Int :$max=50000) {
    mkdir $out-dir unless $out-dir.IO.d;

    for dir($in-dir).grep(*.IO.f) -> $file {
        my $match    = $file ~~ /(\.\w+)[\.gz]?/;
        my $rm-ext   = $match.Str;           # the whole match
        my $ext      = $match.caps[0].value; # just the capture
        my $basename = $file.basename.subst(/$rm-ext $/, '');
        my &next-fh  = sub {
            state $file-num = 1;

            open $*SPEC.catfile(
                $out-dir, 
                sprintf('%s-%03d%s', $basename, $file-num++, $ext)
            ), :w;
        };

        my @buffer;
        my $out-fh = next-fh();
        my $i      = 0;
        my $fh     = $file ~~ /\.gz$/
                     ?? run(«gunzip -c $file |», :out).out
                     !! open $file;

        for $fh.lines -> $line {
            # start of a multi-line record is a ">"
            $i++ if $line ~~ /^'>'/;

            if $i == $max {
                $out-fh.put(@buffer.join("\n")) if @buffer;
                $out-fh.close;
                $out-fh = next-fh();
                $i      = 0;
                @buffer = ();
            }

            @buffer.push($line);
        }

        $out-fh.put(@buffer.join("\n")) if @buffer;
    }
}

=begin pod

=head1 NAME

fasta-split.pl6

=head1 DESCRIPTION

Splits a FASTA file into smaller files each of a "--max" number of 
records.  Useful for breaking large files up for BLAST, etc.

For usage, run with "-h/--help" or no arguments.

For sample FASTA input:

  $ wget ftp://ftp.imicrobe.us/projects/33/samples/713/HUMANGUT_SMPL_F1S.fa.gz

Will process all regular files in "--in-dir."  Handles gzip compressed files
via "gunzip -c."

=head1 SEE ALSO

=item https://en.wikipedia.org/wiki/FASTA_format

=item https://github.com/MattOates/BioInfo

=item BioPerl6

=head1 AUTHOR

Ken Youens-Clark <kyclark@gmail.com>

=end pod
