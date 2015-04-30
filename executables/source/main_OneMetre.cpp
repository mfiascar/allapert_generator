/*
 * Collection of examples of the usage of the 'OneMetre' class
 *
 * 
 *
 */

#include "ReadTwiss.h"
#include "Aperture.h"
#include "OneMetre.h"
//#include "AssignOneMetre.h"

int main ()
{

  /*
  // Test: get aperture definition within OneMetre
  OneMetre Test;
  Test.DefineAperture(0.0, 1, 1, 1, 1);
  Test.DefineAperture(0.1, 2, 2, 2, 2);
  Test.DefineAperture(0.2, 3, 3, 3, 3);
  Test.DefineAperture(0.3, 4, 4, 4, 4);
  Test.DefineAperture(0.99999, .4, .4, .4, .4);
  Test.status();

  vector<double> pos;
  vector<Aperture> pippo;
  Test.GetApertDef(&pos, &pippo);
  for( int i = 0; i < (int) pos.size(); i++){
    cout<<pos[i]<<" "
	<<pippo[i].GetApert(1)<<" "
	<<pippo[i].GetApert(2)<<" "
	<<pippo[i].GetApert(3)<<" "
	<<pippo[i].GetApert(4)<<endl;
  }
  return 0;
  */

  /*
  // Test the assignment of apertures at 0.0 and 1.0
  OneMetre Test;
  Test.empty();
  Test.DefineAperture(0.0, 1, 1, 1, 1);
  Test.DefineAperture(0.1, 2, 2, 2, 2);
  Test.DefineAperture(0.2, 3, 3, 3, 3);
  Test.DefineAperture(0.3, 4, 4, 4, 4);
  Test.status();
  Aperture Pippo = Test.GetAperture( 0.5 );
  Test.status();
  cout<<"Interpolated aperture at 0.5: "<<endl;
  cout<<Pippo.GetApert(1)<<" ";
  cout<<Pippo.GetApert(2)<<" ";
  cout<<Pippo.GetApert(3)<<" ";
  cout<<Pippo.GetApert(4)<<" "<<endl;;
  Pippo = Test.GetAperture( 0.25 );
  cout<<"Interpolated aperture at 0.25:"<<endl;
  cout<<Pippo.GetApert(1)<<" ";
  cout<<Pippo.GetApert(2)<<" ";
  cout<<Pippo.GetApert(3)<<" ";
  cout<<Pippo.GetApert(4)<<" "<<endl;;
  Test.status();
  return 0;
  */

  /*
  // Test the interpolation routine in "GetAperture"
  double p;
  OneMetre Metre;
  Aperture Atmp;
  Metre.DefineAperture(0.0, 3, 3, 3, 3);
  Metre.DefineAperture(0.1, 2, 2, 2, 2);
  Metre.DefineAperture(0.2, 3, 3, 3, 3);
  Metre.DefineAperture(0.3, 4, 4, 4, 4);
  Metre.status();

  ofstream out("StdOneMetre.dat");
  out.precision(4);
  for (int i = 0; i < 100; i++){
    p = (double)(i)/100;
    Atmp.empty();
    Atmp = Metre.GetAperture( p );
    out<<setw(10)<<p;
    out<<setw(10)<<Atmp.GetApert(1);
    out<<setw(10)<<Atmp.GetApert(2);
    out<<setw(10)<<Atmp.GetApert(3);
    out<<setw(10)<<Atmp.GetApert(4)<<endl;
  }
  out.close();
  
  Metre.empty();
  Metre.DefineAperture(0., 1, 1, 1, 1);
  Metre.DefineAperture(0., 2.1, 2.1, 2.1, 2.1);
  Metre.DefineAperture(0.1, 2, 2, 2, 2);
  Metre.DefineAperture(0.2, 3, 3, 3, 3);
  Metre.DefineAperture(0.2, 3.5, 3.5, 3.5, 3.5);
  Metre.DefineAperture(0.7, 4, 4, 4, 4);
  Metre.DefineAperture(0.7, 2, 2, 2, 2);
  Metre.DefineAperture(0.9, 2.5, 2.5, 2.5, 2.5);
  Metre.DefineAperture(0.9999, 2.7, 2.7, 2.7, 2.7);
  Metre.DefineAperture(0.9999, 1, 1, 1, 1);
  Metre.status();

  Atmp = Metre.GetAperture(0.5);
  cout<<Atmp.GetApert(1)<<endl;
  Atmp.empty();

  out.open("SpecialOneMetre.dat");
  out.precision(4);
  for (int i = 0; i <= 200; i++){
    p = (double)(i)/200;
    Atmp.empty();
    Atmp = Metre.GetAperture( p );
    out<<setw(10)<<p;
    out<<setw(10)<<Atmp.GetApert(1);
    out<<setw(10)<<Atmp.GetApert(2);
    out<<setw(10)<<Atmp.GetApert(3);
    out<<setw(10)<<Atmp.GetApert(4)<<endl;
  }
  out.close();
  */

  // More complicated aperture shapes
  OneMetre SinMetre;
  double p;
  Aperture Atmp;
  for (int i = 0; i <= 12; i++){
    p = (double)(i) / 12.1;
    SinMetre.DefineAperture(p, sin(7*p), sin(7*p), 1, 1); // Put it like this to avoid 'Invalid apertures'
  }
  SinMetre.status();

  ofstream out("SinMetre.dat");
  out.precision(4); 
  for (int i = 0; i < 100; i++){
    p = (double)(i)/100.1;
    Atmp.empty();
    Atmp = SinMetre.GetAperture( p );
    out<<setw(10)<<p;
    out<<setw(10)<<Atmp.GetApert(1);
    out<<setw(10)<<Atmp.GetApert(2);
    out<<setw(10)<<Atmp.GetApert(3);
    out<<setw(10)<<Atmp.GetApert(4)<<endl;
  }

  return 0;
}
